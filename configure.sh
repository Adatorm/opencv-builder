cmake -S ./opencv \
 -D CMAKE_BUILD_TYPE=Release \
 -D CMAKE_INSTALL_PREFIX=install \
 -D BUILD_SHARED_LIBS=ON \
 -B ./build \
# -C opencv_options.txt \
