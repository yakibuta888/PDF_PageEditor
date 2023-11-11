#!/bin/bash
set -euxo pipefail

PASSWROD=$(openssl rsautl -decrypt -inkey password.key -in password.txt)
max_retry_count=5 # リトライ回数
retry_interval=3 # リトライ間隔（秒）

sourceDirectry=src/
sourceFileName=main
dockerContext=./docker/pyinstaller/
dockerImageTag=pyinstaller-windows:v1
containerName=pyinst
# pyinstaller option: --hidden-import $hiddenImport
hiddenImport=
# pyinstaller option: --add-binary $addBinary
addBinary=
# ex) "元ファイルパス;取込先ファイルパス"


function retryable() {
  retry_count=0
  while true; do
    "$@" && break

    # リトライ回数が上限に達している場合は、エラーメッセージを出力してリトライ終了
    retry_count=$((retry_count + 1))
    if [ $retry_count -eq $max_retry_count ]; then
      echo "Error: command failed after $max_retry_count attempts"
      break
    fi

    # 待機
    echo "Command failed. Retrying in $retry_interval seconds..."
    sleep $retry_interval
  done
  return $?
}


docker image build -t $dockerImageTag -f "${dockerContext}Dockerfile" "$dockerContext"

retryable docker run --rm --name $containerName -v "$(pwd):/src/" $dockerImageTag -c \
  "/usr/bin/python -m pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org --upgrade pip \
  && /usr/bin/pip install pywin32-ctypes \
  && /usr/bin/pip install --upgrade cffi \
  && /usr/bin/pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org -r env/requirements.txt \
  && pyinstaller $sourceDirectry$sourceFileName.py --onefile --clean --noconsole \
  && mv dist/$sourceFileName.exe $sourceFileName.exe"

echo $PASSWROD | retryable sudo -S rm -rf __pycache__/ build/ dist/ $sourceFileName.spec

docker rmi $dockerImageTag
