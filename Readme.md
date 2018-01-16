Example processing node for [HASTE](http://haste.research.it.uu.se) for use with the [HarmonicIO processing framework](https://github.com/benblamey/HarmonicIO)

**Only works inside a HarmonicIO container (see: https://github.com/benblamey/HarmonicPE)**

## Features
* Caching of storage clients for the HASTE Storage Platform.
* Auto-configuration of HASTE storage client.


## Build and Publish for use in HIO:
```
docker build -t "benblamey/haste-example:latest" . ; docker push benblamey/haste-example:latest
```
