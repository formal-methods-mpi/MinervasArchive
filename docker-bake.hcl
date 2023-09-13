target "docker-metadata-action" {}

target "build" {
  inherits = ["docker-metadata-action"]
  context = "./"
  platforms = [
    "linux/amd64",
    "linux/arm64",
  ]
}
