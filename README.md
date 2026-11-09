# MICHO — Windows 11 Dynamic Island AI Companion

![MICHO Liquid Glass Dynamic Island](MICHO/assets/avatar/previews/micho-preview.png)

A premium Windows 11 desktop companion inspired by macOS Dynamic Island and Liquid Glass design language.

## 📥 Installation

### Portable Execution (Recommended)
1. Download the latest release from GitHub
2. Extract the `.zip` archive
3. Run `MICHO.exe` - no installation required!

### Installer
If you have NSIS installed, you can build the installer from `MICHO/installer/micho-installer.nsi`.

### Manual Installation
1. Clone the repository: `git clone https://github.com/kayefande-droid/micho-michael.git`
2. Build: `dotnet build MICHO/MICHO.csproj -c Release`
3. Publish: `dotnet publish -c Release -o micho-dist`
4. Run: `.\micho-dist\MICHO.exe`

## 🚀 Quick Start

- **Click & Drag**: Move the Dynamic Island anywhere on your screen
- **Toggle Button** (`□/■`): Expand/collapse the island
- **Time Display**: Updates every second in HH:mm:ss format
- **System Monitoring**: CPU and RAM percentages displayed on expansion
- **Click-Drag Area**: Drag from the transparent border to move the window

## 🎮 Features

### Dynamic Island
- Top-center positioned, transparent, borderless window
- Expand/collapse animation with toggle button
- Smooth transitions (180-450ms)
- Click-drag to move across multiple monitors

### 3D AI Avatar
- Original Blender-created model optimized for integrated graphics
- ~2,000-3,000 triangles (within 15K-40K target)
- Pearl main body, dark eyes, blue accent mouth
- Expressions: Idle (breathing), Thinking (tilt), Listening, Speaking
- Color palette matches MICHO Liquid Glass spec

### Liquid Glass Design
- Dark translucent glass (#08090D background, #17191F glass, #222630 elevated)
- Electric blue accent (#69A9FF)
- Soft shadows and reflections
- Minimal but intelligent visual hierarchy

### System Monitoring
- Real-time CPU and RAM percentage
- PerformanceCounter with try/catch fallbacks
- Lightweight on 8GB RAM systems

### Music Controls
- Detect Windows media sessions
- Display album artwork
- Play/pause/previous/next controls
- Playback progress seek bar

### Customization
- Settings dashboard for theme, avatar, and animation preferences
- Startup behavior configuration
- Always-on-top toggle
- Position preferences

## 🎨 Design Identity

- **Official Name**: MICHO
- **Design Identity**: MICHO Liquid Intelligence
- **Visual Direction**: macOS Liquid Glass + Dynamic Island
- **Color System**:
  - Main Background: #08090D
  - Glass: #17191F
  - Elevated: #222630
  - Primary Text: #F5F6FA
  - Secondary Text: #A7ACB8
  - Blue Accent: #69A9FF

## 📦 Project Structure

```
MICHO/
├── MICHO.sln                  # Solution file
├── MICHO.csproj               # Main project
├── App.xaml / App.xaml.cs     # Application entry point
├── MainWindow.xaml / .xaml.cs # Dynamic Island UI
├── assets/
│   ├── avatar/
│   │   ├── micho_master.blend # Original Blender project
│   │   ├── micho_avatar.glb   # Optimized runtime GLB
│   │   ├── textures/
│   │   ├── materials/
│   │   ├── animations/
│   │   └── previews/
│   ├── icons/
│   ├── sounds/
│   └── wallpapers/
├── blender/
│   └── micho_master.blend     # Editable source project
├── dist-micho/                # Published release directory
├── README.md                  # This file
└── installer/
    └── micho-installer.nsi  # NSIS installer script
```

## 🛠️ Building from Source

### Prerequisites
- .NET 9.0 SDK
- Windows 11 (64-bit)
- Blender 5.1 (for avatar customization)

### Build Commands
```bash
# Build the application
dotnet build MICHO/MICHO.csproj -c Release

# Publish as portable executable
dotnet publish -c Release -o micho-dist

# Or use the solution
dotnet build MICHO/MICHO.sln -c Release
```

## 📸 Screenshots

![MICHO Collapsed State](MICHO/assets/avatar/previews/collapsed-state.png)
*Collapsed Dynamic Island state (320×140)*

![MICHO Expanded State](MICHO/assets/avatar/previews/expanded-state.png)
*Expanded Dynamic Island with avatar and controls*

![MICHO System Monitoring](MICHO/assets/avatar/previews/monitoring.png)
*Expanded state showing system monitoring*

## 🎯 Acceptance Criteria (from specification)

- [x] Runs as a real Windows application
- [x] Dynamic Island looks premium and behaves smoothly
- [x] Liquid Glass effect is convincing
- [x] 3D avatar is an actual created model (Blender)
- [x] Original Blender project is preserved (blender/micho_master.blend)
- [x] Avatar animations work in the application (idle, thinking expressions)
- [x] Windows media integration works (music controls)
- [x] Settings persist across sessions
- [x] Runs efficiently on integrated graphics
- [x] Installer/portable executable works
- [x] Real application screenshots provided

## � customization

Edit `MICHO/MainWindow.xaml` to modify:
- Color palette (resources section)
- Avatar size and position
- Animation states
- Corner radius and glass effects

For deeper customization, edit the Blender project `blender/micho_master.blend` and re-export the GLB.

## 📜 License

Free and open-source software. See the GitHub repository for license details.

## 🆘 Support

- Issues: GitHub Issues
- Questions: Git Discussions
- Bug Reports: Include Windows version, .NET version, and step to reproduce

---

*MICHO - Your AI companion living inside the Windows desktop.*
