export function initialize(app) {
  const config = app.lookupFactory ? 
    app.lookupFactory('config:environment') :
    app.__container__.lookupFactory('config:environment');
