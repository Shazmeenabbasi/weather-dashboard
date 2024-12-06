# Use the official Node.js image as the base
FROM node:16 as build

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json (if exists) into the container
COPY package.json /app/

# Install dependencies
RUN npm install

# Copy the rest of the application files
COPY . /app

# Build the application (e.g., for React or similar frontend apps)
RUN npm run build

# Expose the necessary port
EXPOSE 80

# Specify the command to run the app (this might change based on your app)
CMD ["npm", "start"]
