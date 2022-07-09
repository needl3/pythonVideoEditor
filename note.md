# TODO
    - Implement filter function #
        - [ https://zulko.github.io/moviepy/ref/videofx.html ]
    - Implement basic render function #
    - Implement audio functions
        - Adding in final concatinated file
        - Adding in individual clips
    - Implement downloading videos from
        - FaceBook
        - Instagram
        - TikTok

```python
        # Pass to corresponding handler
        {
          "fadein":applyFade(clip),
          "fadeout":applyFade(clip, out=True),
          "crop":applyCrop(clip),
          "changeSpeed": changeSpeed(clip),
          "reverseClip": reverseClip(clip),
          "rotateClip": rotateClip(clip),
          "resizeClip": resizeClip(clip),
          "Back": void()
        }

```

```python
context ={
    "videos":{
        int(): {
            "name":str(),
            "path":str()
        }
    },
    "audio":{
        int(): {
            "name":str(),
            "path":str()
        }
    },
    "filters":{
        int():list()
    },
    "clips":{
        int():{
              "_id":int(), #It's id from "videos"
              "portion":["from", "to"]
		}
    },
    "concat":[int()]
}
```