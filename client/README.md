# Client Mobile App

The frontend is written using React Native with Expo.

The app can be tested using Expo Go, general directions are listed in the root README.

## Structure overview

The app contains a dozen of components, interconnected by navigation supplied by @expo-router

The client has a clear separation of state by using contexts that trickle down to the relevant components:\
    - Authentication Context : tracks authentication state\
    - Portfolio Context : persists the portfolios of users for a session

## Local Deployment

One caveat not mentioned in the root README is that we need to substitute the SERV_IP/PORT in the .env file
of the expo app.
