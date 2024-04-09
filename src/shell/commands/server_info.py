def server_info(si):
    # Récupération des informations de l'hôte connecté
    content = si.RetrieveContent()
    about = content.about

    print("Server Information:")
    print("-------------------")
    print("Product Name:", about.fullName)
    print("Product Version:", about.version)
    print("Vendor:", about.vendor)
    print("Build:", about.build)
    print("Instance UUID:", about.instanceUuid)
    print("License Product Name:", about.licenseProductName)
    print("License Product Version:", about.licenseProductVersion)

    # Récupération des informations sur les hôtes
    host_view = content.viewManager.CreateContainerView(content.rootFolder, [vim.HostSystem], True)
    hosts = host_view.view
    host_view.Destroy()

    print("\nHost Information:")
    print("-----------------")
    for host in hosts:
        print("Host:", host.name)
        print("IP Address:", host.summary.managementServerIp)
        print("Bios Version:", host.hardware.systemInfo.biosInfo.biosVersion)
        print("CPU Model:", host.hardware.cpuModel)
        print("CPU Cores:", host.hardware.cpuInfo.numCpuCores)
        print("Memory:", round(host.hardware.memorySize / (1024 * 1024 * 1024), 2), "GB")
        print("")