target "docker-metadata-action" {}

target "build" {
  secret = ["id=env.json,src=.env"]
  inherits = ["docker-metadata-action"]
  context = "./"
  dockerfile = "Dockerfile"
  platforms = [
    "linux/amd64",
    "linux/arm64",
  ]
}
