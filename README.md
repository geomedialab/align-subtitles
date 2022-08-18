# align-subtitles

This small Python script replaces the timestamps of one subtitle file with the timestamps of another in order of appearance.

The script was created in the context of the [atlascine project](https://github.com/geomedialab/atlascine), which publishes media featuring annotated subtitles in multiple languages. In this interface, for the annotations to appear consistently across multiple subtitle language version, timestamps have to be the same.

For example, given the following inputs:
```
00:00:05.100 --> 00:00:06.040
They went home

00:00:06.040 --> 00:00:07.088
that day
```
and
```
00:00:05.290 --> 00:00:06.039
They went home

00:00:06.039 --> 00:00:08.000
that day
```

The script will produce:
```
00:00:05.100 --> 00:00:06.040
They went home

00:00:06.040 --> 00:00:07.088
that day
```


