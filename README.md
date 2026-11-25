# Mock Finance App: [![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


The app is a demo of a finance app that let's one trade securities.

The client is for mobile, written with [React Native](https://reactnative.dev/).

The server is written with [.NET](https://dotnet.microsoft.com/en-us/).

Both the client and server subfolders contain more specific READMEs relevant to their respective domains.

# Local Deployment

The app was designed with IOS mainly in mind, publishing to the App Store wasn't time efficient.

The server can be run with:
```
dotnet run
```
We prebuild the source files:

```
npx expo prebuild --clean
```
Then, the client can be started in an emulator using:
```
npx expo run:ios
```


## Licensing

[MIT](https://choosealicense.com/licenses/mit/)