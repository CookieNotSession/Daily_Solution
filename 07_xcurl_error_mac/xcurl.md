# 20190321 MacOS Update and the xcrun error

- invalid active developer path, missing xcrun

Solution
===
```
xcode-select --install
```
if the command is not work , try these command down below.
```
sudo xcode-select -switch /
```