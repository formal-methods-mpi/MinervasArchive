target "docker-metadata-action" {}

target "build" {
  secret = ["id=env,src=./.env"]
  inherits = ["docker-metadata-action"]
  context = "./"
  platforms = [
    "linux/amd64",
    "linux/arm64",
  ]
}
