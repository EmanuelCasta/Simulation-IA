from controller.controllerMagnazited import controllerMagnazited

if __name__ == "__main__":

    
    #Database
   
    program = controllerMagnazited()
    program.put_information()

    #Parameters
    headless = True                    # True = No Chrome GUI
    number_of_workers = 1       