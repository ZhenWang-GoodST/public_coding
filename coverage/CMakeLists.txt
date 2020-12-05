cmake_minimum_required(VERSION 2.8.3)
project(coverage_test)
add_compile_options(-std=c++11)
set(ROOT ~/company/coding)
set(ROOTPATH ${ROOT}/planning_algorithm)
set(ROOTPATH_COVERAGE ${ROOTPATH}/coverage_planners)
set(ROOTPATH_P2P ${ROOTPATH}/p2p_planners)
set(ROOTPATH_SMOOTH ${ROOTPATH}/smoother)
set(ROOTPATH_SPEED ${ROOTPATH}/speed_generator)

message(STATUS ${ROOTPATH})
message(STATUS ${ROOTPATH_COVERAGE})
message(STATUS ${ROOTPATH_P2P})
message(STATUS ${ROOTPATH_SMOOTH})
message(STATUS ${ROOTPATH_SPEED})

# find_package(Gflags)
find_package(ompl)
find_package(OpenCV REQUIRED)
find_package(Eigen3 REQUIRED)
find_package(glog 0.4.0 REQUIRED)
# find_package(CGAL REQUIRED)
find_package(CGAL COMPONENTS Core)

# include_directories(${GFLAGS_INCLUDE_DIRS} ${GLOG_INCLUDE_DIRS})
include_directories(${GLOG_INCLUDE_DIRS})
include_directories(${ROOT})
include_directories(${ROOTPATH})
include_directories(${OMPL_INCLUDE_DIRS} ${OpenCV_INCLUDE_DIRS} ${EIGEN3_INCLUDE_DIR})


#add lib
file(GLOB_RECURSE ${TERGEO_LIB_NAME_UPPER}_SRC "./*.cpp")

message(STATUS ${TERGEO_LIB_NAME_UPPER}_SRC)
ADD_LIBRARY(cov_lib SHARED 
    ${ROOTPATH_COVERAGE}/base_coverage_planner.cpp
    # ${ROOTPATH_COVERAGE}/coverage_planner_factory.cpp
    ${ROOTPATH_COVERAGE}/common_function/coverage_utils.cpp
    ${ROOTPATH_COVERAGE}/common_function/iGraph.cpp
    ${ROOTPATH_COVERAGE}/common_function/linear_Planner.cpp
    ${ROOTPATH_COVERAGE}/common_function/param_reader.cpp
    ${ROOTPATH_COVERAGE}/common_function/polygon_partition.cpp
    ${ROOTPATH_COVERAGE}/common_function/polygon_partition4.cpp
    ${ROOTPATH_COVERAGE}/uturn_interlaced_planner/uturn_interlaced_planner.cpp
    ${ROOTPATH_COVERAGE}/uturn_interlaced_planner/uturn_interlaced_planner.cpp
)
TARGET_LINK_LIBRARIES(cov_lib 
glog::glog ${CGAL_LIBS} ${OMPL_LIBRARIES} ${OpenCV_LIBS} CGAL::CGAL CGAL::CGAL_Core)

ADD_LIBRARY(p2p SHARED 
    ${ROOTPATH_P2P}/astar/astar.cpp
    ${ROOTPATH_P2P}/astar/distance_map.cpp
)
TARGET_LINK_LIBRARIES(cov_lib 
glog::glog ${CGAL_LIBS} ${OMPL_LIBRARIES} ${OpenCV_LIBS} CGAL::CGAL CGAL::CGAL_Core)

#add executable
add_executable(coverage_test coverage_test.cpp)
target_link_libraries(coverage_test 
    cov_lib p2p glog::glog 
    ${CGAL_LIBS} ${OMPL_LIBRARIES} 
    ${OpenCV_LIBS} CGAL::CGAL CGAL::CGAL_Core
    )
