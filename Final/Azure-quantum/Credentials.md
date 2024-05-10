## Credentials 

### Installation

[Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-macos#install-with-homebrew)

In your powershell, run the following command:

```
brew update && brew install azure-cli
```

### Login

In your powershell, run the following command:

```
az login
```

### Run

In your terminal, locate your server folder and run the following command:

```
uvicorn main:app --reload
```

Note: Do not use VS Code Terminal. 