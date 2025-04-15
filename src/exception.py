import sys 
 
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()#exc_info has all the error details and exc_tb provides all the file information

    file_name= exc_tb.tb_frame.f_code.co_filename
    error_message="Error occurred python script name [{0}] line number [{1}] error message [{2}] ".format(
        file_name,exc_tb.tb_linneno,str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_detail: sys):
        super().__init__(error_message)
        self.error_message= error_message_detail(
            error_message,error_detail=error_detail
        )

    def __str__(self):#onlly for display
        return self.error_message
