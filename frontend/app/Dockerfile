# Use the official Node.js image to build the frontend
FROM node:16 as build

# Set the working directory inside the container
WORKDIR /app

# Copy the package.json and package-lock.json files
COPY package.json package-lock.json /app/

# Install dependencies
RUN npm install

# Copy the application source code
COPY . /app/

# Build the frontend
RUN npm run build

# Serve the frontend using a lightweight web server (e.g., Nginx)
FROM nginx:1.23-alpine

# Copy the build output to the Nginx HTML directory
COPY --from=build /app/build /usr/share/nginx/html

# Expose the port on which Nginx runs
EXPOSE 80

# Start the Nginx server
CMD ["nginx", "-g", "daemon off;"]
