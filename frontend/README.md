# Frontend README

This is the frontend directory of the Motivation App project. It contains the React frontend application that displays a list of motivation sentences.

## Project Structure

The frontend directory has the following structure:

- `src/App.js`: This file is the main component of the React frontend application. It renders the `MotivationList` component and handles the logic for fetching and displaying motivation sentences.

- `src/index.js`: This file is the entry point of the React frontend application. It renders the `App` component and mounts it to the DOM.

- `src/components/MotivationList.js`: This file exports a React component `MotivationList` which displays a list of motivation sentences. It receives the list of sentences as props and renders them.

- `src/styles/App.css`: This file contains the CSS styles for the `App` component.

## Getting Started

To run the frontend application, follow these steps:

1. Make sure you have Node.js and npm installed on your machine.

2. Install the dependencies by running the following command in the terminal:

   ```
   npm install
   ```

3. Start the development server by running the following command:

   ```
   npm start
   ```

   This will start the application and open it in your default browser.

## Dependencies

The frontend application has the following dependencies:

- React: A JavaScript library for building user interfaces.
- React DOM: A package for rendering React components in the browser.
- Axios: A promise-based HTTP client for making API requests.

These dependencies are listed in the `package.json` file.

## Contributing

If you would like to contribute to this project, please follow the guidelines in the [CONTRIBUTING.md](../CONTRIBUTING.md) file.

## License

This project is licensed under the [MIT License](../LICENSE).

For more information, please refer to the [backend README](../backend/README.md).