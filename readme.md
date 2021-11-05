# cyberpunk2077 r6-config-editor
[![CD](https://github.com/rdok/cyberpunk2077-r6-config-editor/workflows/CD-stable/badge.svg)](https://github.com/rdok/cyberpunk2077-r6-config-editor/actions?query=workflow%3ACD)
[![nexus-mods](https://img.shields.io/badge/Nexus%20-Mods-orange?style=flat-square&logo=spinrilla)](https://www.nexusmods.com/cyberpunk2077/mods/341)


Modifies Cyberpunk 2077 to map buttons to increase usability.

### Development
> Dependency: [Docker](https://www.docker.com/)

```
make shell
make test-watch
```

##### Windows OS
###### Local Build
```
.\scripts\build.ps1
```

### Release
> Each PR creates an executable artifact. Use this artifact to test your release.

Once merged to main branch:

```
git tag -a v1.0.0 # Add headline & content on prompt
git push origin v1.0.0
```

The CI/CD pipeline will pick up the tag change and create a new release.