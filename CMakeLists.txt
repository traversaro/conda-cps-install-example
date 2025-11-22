cmake_minimum_required(VERSION 4.1)

project(conda_cps_install_example LANGUAGES C CXX)

include(FetchContent)

FetchContent_Declare(cps_examples_zwrap
    GIT_REPOSITORY https://github.com/cps-org/cps-examples.git
    GIT_TAG e857eb8a46a300b9e594aaf8a9853c0c736f5dde
    SOURCE_SUBDIR "cmake/zdemo/zwrap"
)

FetchContent_MakeAvailable(cps_examples_zwrap)
