#include "planning_algorithm/coverage_planners/base_coverage_planner.h"
#include "planning_algorithm/coverage_planners/uturn_interlaced_planner/uturn_interlaced_planner.h"
#include "planning_algorithm/coverage_planners/common_function/param_reader.h"

#include <iostream>
using namespace tergeo::planning::algorithm;
// typedef tergeo::planning::algorithm TPA;
std::string root_path = "/home/tl/hdmap_test/maps/floor_3-200818/floor_3";
std::string map_name = "/floor_3";
std::string map_path = root_path + map_name + ".jpg";
std::string tfw_path = root_path + map_name + ".tfw";
std::string cfg_file = "/home/tl/bow_shape_planner.cfg";
int count = 100;

void read(std::string cfg_file) {
    ParamReader reader;
    if(reader.loadParam(cfg_file)){
        std::string bo, ls;
        // if(reader.getValue("root_path", bo)){
        //     root_path = bo.c_str();
        // }
        // if(reader.getValue("root_path", bo)){
        //     root_path = atof(bo.c_str());
        // }
        if(reader.getValue("count", bo)){
            count = atoi(bo.c_str());
        }
    }
}

int main()
{
    read(cfg_file);
    google::InitGoogleLogging("loging");
    FLAGS_log_dir = "/home/tl/tmp"; 
    LOG(INFO) << "\nGLOG: hello world";
    std::vector<Point> outpoly = {};
    outpoly.emplace_back(Point(-10.901655629139073, -1.5953642384105962));
    outpoly.emplace_back(Point(-4.3429359823399558, -7.7552428256070645));
    outpoly.emplace_back(Point(9.306291390728477, 6.6473509933774837));
    outpoly.emplace_back(Point(-4.9190397350993385, 19.543211920529803));
    outpoly.emplace_back(Point(-10.813024282560708, 12.895860927152318));
    outpoly.emplace_back(Point(-5.8053532008830029, 8.37566225165563));
    outpoly.emplace_back(Point(-1.1078918322295805, 13.516280353200884));
    outpoly.emplace_back(Point(6.470088300220751, 6.603035320088301));
    outpoly.emplace_back(Point(-0.088631346578366452, -0.53178807947019868));
    outpoly.emplace_back(Point(-5.2735651214128039, 4.5201986754966894));
    
    for (size_t i = 0; i < count; ++i) {
        UTInterlacedPlanner UTIPlanner(cfg_file);
        UTIPlanner.loadMap(map_path, tfw_path);
        Trajectory tra;
        std::vector<Point> outline = {};
        outline = outpoly;
        std::vector<std::vector<Point>> exclude_poly = {};
        UTIPlanner.planOnPolygon(outline, exclude_poly, tra); 
        std::cout << "\nfinished the --------------------- " << i << "----------------------------time\n\n";
    }
    
    google::ShutdownGoogleLogging();
    std::cout << "coverage test\n";
    return 0;
}