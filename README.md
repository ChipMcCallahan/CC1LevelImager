# CC1LevelImager

Basic imaging functionality for CC1 levels. Not intended to be full featured.

Uses CC2 artwork at present and will probably stay that way unless more features are needed.


To get started, try the demo [Colab notebook](https://github.com/ChipMcCallahan/CC1LevelImager/blob/main/cc1_levelset_displayer.ipynb)

or use these snippets:

```
pip install git+https://github.com/ChipMcCallahan/CC1LevelImager.git
pip install git+https://github.com/ChipMcCallahan/CC1LevelsetIO.git
```

```
from cc1_levelset_io.cc1_levelset_reader import CC1LevelsetReader
from cc1_level_imager.cc1_level_imager import CC1LevelImager
import IPython.display as ipd

reader = CC1LevelsetReader()
s = reader.import_and_read("JBLP1.dat")

imager = CC1LevelImager()   
img = imager.save_png(s.levels[0], "temp.png")
```

![jplp1_level1](https://user-images.githubusercontent.com/87612918/126425565-f8f532e8-b64a-43a1-9e71-b9d3791c2e81.png)
