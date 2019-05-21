# PyJyutping

Chinese text to [Jyutping](https://en.wikipedia.org/wiki/Jyutping) 
(粵拼; a standard of Cantonese romanization) conversion library in Python. 
Conversion is based on an officially published [Cantonese Pronunciation List](http://www.iso10646hk.net/jp/document/jyut_yam_table.jsp). 
This library performs the conversion using the Jyutping romanization table 
prepared by [Dr. Samuel Cheng](https://www.samuelcheng.info/jyutping.html), 
which has been further converted to a [dictionary file in JSON format](pyjyutping/data/jyutping_dictionary.json).


## Installation

```shell
pip install pyjyutping
```


## Usage

### Python

```python
>>> from pyjyutping import jyutping
>>> jyutping.convert("我係香港人")
'ngo5 hai6 hoeng1 gong2 jan4'
```

Tone number in output can be disabled:

```python
>>> jyutping.convert("我係香港人", tone=False)
'ngo hai hoeng gong jan'
```

Alphabets and digits are preserved in the conversion:

```python
>>> jyutping.convert("香港嘅英文係Hong Kong")
'hoeng1 gong2 ge3 jing1 man4 hai6 Hong Kong'
>>> jyutping.convert("1841年1月25號香港開埠")
'1841 nin4 1 jyut6 25 hou6 hoeng1 gong2 hoi1 bou6'
```

### Command-Line Interface Tool

```shell
$ pyjyutping 我係香港人
ngo5 hai6 hoeng1 gong2 jan4
```


## License

MIT
