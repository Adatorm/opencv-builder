# opencv-builder

to compile opencv without unused modules;
<br>
copy options/opencv_options.txt to opencv directory

then run cmake with:

```
cmake -C opencv_options.txt ...
```

>Note: 
**opencv_options.txt** contains only excluded modules. Other cmake configurations should be provided by the developer. (build directory etc.)

## build opencv library

To build opencv library for various platform with excluded modules

go to github actions tab

![Alt text](assets/repo.png?raw=true "repository")


then select the build action

![Alt text](assets/gitactions.png?raw=true "gitactions")

<br>
<br>

- 1 - open manuel event trigger panel
- 2 - select branch
- 3 - type opencv version tag
- 4 - start the workflow

![Alt text](assets/actionparameter.png?raw=true "gitactions")

<br>

### issues

<br>

If the build failed you need to remove the last inserted tag and release if you want to rebuild the same library with the same version.

<br>

  - 4.4.0 failed (ios build script error)
  - 3.4.16 failed (ios build script error)
  - 4.5.0 failed (ios build script error)
  
