grass:
    sudo apt update
    sudo apt install -y python3 python3-pip unzip
    
    pip3 install webdriver_manager

    python3 -c "from webdriver_manager.chrome import ChromeDriverManager; ChromeDriverManager().install()"
