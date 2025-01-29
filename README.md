# mineops

A Python-based FTB (Feed The Beast) Minecraft Server Manager that automates the process of downloading, installing, and managing modded Minecraft servers. Currently focused on the All The Mods 10 (ATM10) modpack.

## Features

- Automated download of the latest ATM10 server files from CurseForge
- Smart file management with automatic version checking
- Extraction and organization of server files
- Prevents duplicate downloads of existing server versions

## Prerequisites

1. Python 3.x
2. CurseForge API Token (required for accessing modpack files)
3. Sufficient disk space for server files

## Installation

1. Clone this repository:
```bash
git clone https://github.com/shallotpancake/mineops.git
cd mineops
```

2. Create a `.curseforge_api_token` file in the root directory containing your CurseForge API token:
```bash
echo "your-api-token-here" > .curseforge_api_token
```

3. Install the required Python packages:
```bash
pip install requests
```

## Usage

To download and install the latest ATM10 server:

```bash
python3 main.py
```

The script will:
1. Check for the latest ATM10 server version
2. Download the server files if a newer version is available
3. Extract the files to the `server` directory
4. Organize the files for server operation

## Project Structure

```
mineops/
├── const.py              # Global constants and path configurations
├── main.py              # Main entry point
├── curseforge/          # CurseForge API interaction
│   ├── const.py         # CurseForge-specific constants
│   ├── curseforge.py    # Core CurseForge functionality
│   └── helpers.py       # Helper functions for API interaction
└── minecraft/           # Minecraft server management
    └── install.py       # Server installation logic
```

## Configuration

The project uses several directories that are automatically created:

- `server/`: Contains the extracted server files
- `downloads/`: Stores downloaded server pack files
- `logs/`: Contains operation logs

## Technical Details

### CurseForge API Integration

The project uses the CurseForge API v1 to:
- Search for modpacks
- Retrieve latest server files
- Download server packs

API endpoints used:
- `/mods/search`: For finding modpack IDs
- `/mods/{id}/files/`: For retrieving file information
- `/mods/{id}/files/{fileId}/download-url/`: For getting download URLs

### File Management

The system implements smart file management:
- Checks for existing server installations
- Prevents duplicate downloads
- Automatically organizes extracted files
- Handles nested directories during extraction

## Roadmap

### Completed
- Basic server pack downloading
- File extraction and organization
- Version checking
- Directory structure management

### Planned
- Server update functionality
- Multiple modpack support
- Server configuration management
- Automated backup system
- Server start/stop controls

## Contributing

Contributions are welcome! Please feel free to submit pull requests or create issues for bugs and feature requests.

## License

See the [LICENSE](LICENSE) file for details.