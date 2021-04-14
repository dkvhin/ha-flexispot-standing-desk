import machine
import flexispot

def main():
    f = flexispot.ControlPanel(publish_discovery=False, debug=False)
    f.listen_mqtt()
    
       
if __name__ == '__main__':
    main()
