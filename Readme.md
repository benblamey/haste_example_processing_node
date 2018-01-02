Example processing node for [HASTE](http://haste.research.it.uu.se) for use with the [HarmonicIO processing framework](https://github.com/benblamey/HarmonicIO)


### Build and Publish for use in HIO:
```
docker build -t "haste-example" . 
docker tag haste-example benblamey/haste-example:latest 
docker push benblamey/haste-example
```