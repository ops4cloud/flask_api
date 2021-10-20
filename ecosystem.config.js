module.exports = {
  apps : [{
    name   : "flask_api",
    script : "flask_api/app.py",
    interpreter: "python3",
      env: {
        COMMON_VARIABLE: "true"
      },
      env_production: {
        NODE_ENV: "production"
      }
  }]
}