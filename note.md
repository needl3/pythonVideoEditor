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
    print("Concatenate video from?".center(40, "-"))
    print("1. Unedited/Unfiltered clips\n\
        2. Edited/Filtered clips")
    _=None
    while _ != 1 or _ != 2:
        try:
            _ = int(input("Input appropriate option\n=>"))
        except ValueError:
            print("Invalid option")

    c = None
    case 1:
        c = context.get()
    case 2:
        c = context.get("clips")
    case _:
        print("Invalid option. Going back")     
        return
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
    "clips":{
        int():{
              "_id":int(), #It's id from "videos"
              "portion":["from", "to"],
              "filters": []
		}
    },
    "concat":[int()]
}
```