#include "planning_algorithm/coverage_planners/base_coverage_planner.h"
#include "planning_algorithm/coverage_planners/uturn_interlaced_planner/uturn_interlaced_planner.h"
#include "planning_algorithm/coverage_planners/common_function/param_reader.h"
#include <task/task.h>
#include <task/proto/task.pb.h>
#include <common/file.hpp>
#include <iostream>
using namespace tergeo::planning::algorithm;
// typedef tergeo::planning::algorithm TPA;
std::string root_path = "/home/tl/hdmap_test/maps/floor_3-200818/floor_3";
std::string map_name = "/floor_3";
std::string map_path = root_path + map_name + ".jpg";
std::string tfw_path = root_path + map_name + ".tfw";
std::string cfg_file = "/home/wz/bow_shape_planner.cfg";
int count = 100;

void read(std::string cfg_file) {
    ParamReader reader;
    if(reader.loadParam(cfg_file)){
        std::string bo, ls;
        if(reader.getValue("root_path", bo)){
            root_path = bo.c_str();
        }
        if(reader.getValue("map_name", bo)){
            map_name = bo.c_str();
        }
        if(reader.getValue("count", bo)){
            count = atoi(bo.c_str());
        }
    }
    map_path = root_path + map_name + ".jpg";
    tfw_path = root_path + map_name + ".tfw";
}
std::vector<Point> loaddata(const std::string& path) {
    std::vector<Point> poly = {};
    // std::string task_path = path;
    // tergeo::task::proto::Task proto_task;
    // tergeo::common::file::GetProtoFromASCIIFile(task_path, proto_task);
    // tergeo::task::Task task;
    // task.fromProto(proto_task);
    // auto &points = task.reference_line.points;
    // for (size_t i = 0; i < points.size(); ++i) {
    //     double x = points[i].pose.x;
    //     double y = points[i].pose.y;
    //     poly.emplace_back(Point(x, y));
    // }
    return poly;
}
void print(std::vector<Point> &poly) {
    for (size_t i = 0; i < poly.size(); ++i) {
        double x = poly[i].x;
        double y = poly[i].y;
        std::cout << "( " << x << " " << y << " )\n";
    }
}

int main()
{
    read(cfg_file);
    google::InitGoogleLogging("loging");
    FLAGS_log_dir = "/home/tl/tmp"; 
    LOG(INFO) << "\nGLOG: hello world";
    std::vector<Point> outpoly = {};
    std::vector<std::vector<Point>> inpolys = {};
    // loaddata("/home/wz/Downloads/gc_indoor/gc_indoor_in_1.task");
    // outpoly.emplace_back(Point(-10.901655629139073, -1.5953642384105962));
    // outpoly.emplace_back(Point(-4.3429359823399558, -7.7552428256070645));
    // outpoly.emplace_back(Point(9.306291390728477, 6.6473509933774837));
    // outpoly.emplace_back(Point(-4.9190397350993385, 19.543211920529803));
    // outpoly.emplace_back(Point(-10.813024282560708, 12.895860927152318));
    // outpoly.emplace_back(Point(-5.8053532008830029, 8.37566225165563));
    // outpoly.emplace_back(Point(-1.1078918322295805, 13.516280353200884));
    // outpoly.emplace_back(Point(6.470088300220751, 6.603035320088301));
    // outpoly.emplace_back(Point(-0.088631346578366452, -0.53178807947019868));
    // outpoly.emplace_back(Point(-5.2735651214128039, 4.5201986754966894));
    
    outpoly.emplace_back(Point( 40.889819548495595, -44.560920826010957));
    outpoly.emplace_back(Point( 51.912538249439528, 34.401318902913644));
    outpoly.emplace_back(Point( -10.526345917077784, 43.24955170277611));
    outpoly.emplace_back(Point( -10.787870039241207, 41.331708140244345));
    outpoly.emplace_back(Point( -53.899354440456484, 47.311457193510996));
    outpoly.emplace_back(Point( -63.515491802756621, -25.873453152701295));
    outpoly.emplace_back(Point( -72.890887493134869, -24.566250980479719));
    outpoly.emplace_back(Point( -73.511292450672173, -29.067534431390559));
    std::vector<Point> tempoly = {};
    tempoly.emplace_back(Point( -50.801060730244707, 43.587353693903651));
    tempoly.emplace_back(Point( -23.836834051353552, 39.800702341745755));
    tempoly.emplace_back(Point( -33.771481642036527, -29.961946929189349));
    tempoly.emplace_back(Point( -59.950046270595, -26.257021865207523));
    inpolys.emplace_back(tempoly);
    tempoly.clear();

    tempoly.emplace_back(Point( -20.900136096226753, 39.392070900865335));
    tempoly.emplace_back(Point( 5.6357086221414319, 35.636066906773465));
    tempoly.emplace_back(Point( -3.9501039285100044, -34.222883173728917));
    tempoly.emplace_back(Point( -30.912151239716348, -30.371668053911947));
    inpolys.emplace_back(tempoly);
    tempoly.clear();

    tempoly.emplace_back(Point( 9.0996446559687971, 35.176737925127696));
    tempoly.emplace_back(Point( 33.213563514754263, 31.753387166008508));
    tempoly.emplace_back(Point( 23.449298889660827, -38.038857918084112));
    tempoly.emplace_back(Point( -1.2720533302028714, -34.574186347663129));
    inpolys.emplace_back(tempoly);
    tempoly.clear();

    tempoly.emplace_back(Point( 36.337207629874094, 31.304786121790812));
    tempoly.emplace_back(Point( 47.704231555116756, 29.699097751473328));
    tempoly.emplace_back(Point( 37.956800212592427, -40.101262530739568));
    tempoly.emplace_back(Point( 26.28017546748945, -38.458180255859126));
    inpolys.emplace_back(tempoly);  
    tempoly.clear();
    std::cout<< map_path << "\n";
    std::cout<< tfw_path << "\n";
    for (size_t i = 0; i < count; ++i) {
        UTInterlacedPlanner UTIPlanner(cfg_file);
        UTIPlanner.loadMap(map_path, tfw_path);
        Trajectory tra;
        std::vector<Point> outline = {};
        outline = outpoly;
        std::vector<std::vector<Point>> exclude_poly = {};
        exclude_poly = inpolys;
        UTIPlanner.planOnPolygon(outline, exclude_poly, tra); 
        std::cout << "\nfinished the --------------------- " << i << "----------------------------time\n\n";
    }
    std::cout << std::min(0, -1) <<"\n";
    google::ShutdownGoogleLogging();
    std::cout << "coverage test\n";
    return 0;
}