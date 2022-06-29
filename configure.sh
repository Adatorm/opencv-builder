cmake -S ./opencv \
 -D CMAKE_BUILD_TYPE=Release \
 -D CMAKE_INSTALL_PREFIX=install \
 -B ./build \
 -C opencv_options.txt \