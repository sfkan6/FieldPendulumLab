FROM node:lts-alpine AS requirements-stage

WORKDIR /app

ENV PATH="/app/node_modules/.bin:$PATH"

COPY package-lock.json .
COPY package.json .
RUN npm install


FROM requirements-stage AS development-stage
COPY . .
RUN npm run build

FROM development-stage AS production-stage

# sudo docker build --target development-stage -t frontend .
# sudo docker run -p 5000:5000 frontend
CMD ["npm", "run", "dev"]
