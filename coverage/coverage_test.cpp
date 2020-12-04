#include "planning_algorithm/coverage_planners/base_coverage_planner.h"
#include <iostream>
int main()
{
    google::InitGoogleLogging("loging");
    FLAGS_log_dir = "/home/wz/tmp"; 
    LOG(INFO) << "\nGLOG: hello world";
    google::ShutdownGoogleLogging();
    std::cout << "coverage test\n";
}