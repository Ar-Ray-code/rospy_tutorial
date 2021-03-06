#!/bin/python3
import rospy
from original_msg_srv.msg import ExampleMsg
from original_msg_srv.srv import CalcMsgSrv, CalcMsgSrvResponse

class service_server:
    def __init__(self):
        rospy.Service('calc_ab',CalcMsgSrv,self.srv_ab)
        rospy.spin()
    
    def calc_four_arithmetic_operations(self, input_a, input_b):
        msg_data = ExampleMsg()
        msg_data.a              = input_a
        msg_data.b              = input_b
        msg_data.sum_ab         = input_a + input_b
        msg_data.diff_ab        = input_a - input_b
        msg_data.product_ab     = input_a * input_b

        if(input_b == 0):
            msg_data.quotient_ab   = 0
            msg_data.remainder_ab  = 0
        else:
            msg_data.quotient_ab    = input_a // input_b
            msg_data.remainder_ab   = input_a % input_b
        return msg_data

    def srv_ab(self,request):
        result = self.calc_four_arithmetic_operations(request.a,request.b)
        return CalcMsgSrvResponse(result)

def rospy_init(args = None):
    rospy.init_node('service_server',argv=args)
    service_server()
    
if __name__=="__main__":
    rospy_init()
