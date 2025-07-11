# Portable Standalone Depth Map UI

![UI Screenshot]([https://raw.githubusercontent.com/cyberhirsch/Depth_portable/main/screenshot/screenshot.png])

This project provides a portable, standalone graphical user interface (GUI) for the powerful **[stable-diffusion-webui-depthmap-script](https://github.com/thygate/stable-diffusion-webui-depthmap-script)**. It allows you to generate depth maps, 3D stereo images, normal maps, and even 3D meshes from a single image, all from a self-contained folder that can be run on any Windows machine without a full installation of Stable Diffusion WebUI.

This package includes the necessary scripts and configurations to build this portable environment.

## Features

*   **Standalone GUI:** A full-featured Gradio interface that runs locally in your browser.
*   **Multiple Models:** Supports a wide range of state-of-the-art monocular depth estimation models, including MiDaS, ZoeDepth, Marigold, and Depth Anything V2.
*   **Portable:** The entire application, including Python and all dependencies, is contained within a single folder. Perfect for running from a USB drive or moving between computers.
*   **Versatile Outputs:** Generate not just depth maps, but also:
    *   3D Stereoscopic Images (side-by-side or anaglyph).
    *   Normal Maps for use in 3D rendering.
    *   Simple and advanced 3D Meshes (.ply or .obj).
    *   Videos from the generated 3D meshes.
*   **Background Removal:** Integrated `rembg` functionality.

## Installation and Setup

Follow these steps to set up the portable application. This only needs to be done once.

**1. Download this Repository**

Click the green `<> Code` button on the main GitHub page and select **Download ZIP**. Extract the contents of the ZIP file to a location of your choice.

**2. Download Portable Python**

This application requires a specific "embeddable" version of Python.

*   Go to the Python downloads page: [**https://www.python.org/downloads/windows/**](https://www.python.org/downloads/windows/)
*   Find a stable version, such as **Python 3.10.11**.
*   Scroll down and download the file named **"Windows embeddable package (64-bit)"**.

**3. Set Up the Folder Structure**

*   Extract the contents of the Python ZIP file you just downloaded.
*   Rename the extracted folder to `python-3.10.11-embed-amd64`.
*   Place this folder inside the main project directory, alongside the `stable-diffusion-webui-depthmap-script-main` folder.

Your final folder structure should look like this:
Markdown
Portable-Depth-Map-UI/
├── python-3.10.11-embed-amd64/
│ ├── python.exe
│ └── ... (other python files)
└── stable-diffusion-webui-depthmap-script-main/
├── gui.py
└── ... (other script files)
├── Run_Depth_Portable.bat
├── setup.bat
└── README.md
Generated code
**4. Run the Setup Script**

Double-click the **`setup.bat`** file. This will automatically:
*   Enable the package manager (`pip`) for the portable Python.
*   Install all the necessary libraries (`torch`, `gradio`, `timm`, `transformers`, etc.) into the portable Python environment.

This step will take several minutes and requires an internet connection.

## How to Use

1.  Double-click **`Run_Depth_Portable.bat`**.
2.  A command prompt window will appear and start the local web server.
3.  Once you see the message `Running on local URL: http://127.0.0.1:7860`, open your web browser and navigate to that address.
4.  Use the interface to generate your depth maps and other outputs!

**Note:** The first time you use a specific depth model, it will be downloaded automatically. This may take a moment. Subsequent uses will be much faster. The models are saved inside the `stable-diffusion-webui-depthmap-script-main/models` folder, keeping them part of your portable package.

---

## UI Options Explained

The interface is divided into several sections for different functionalities.

### Main Settings

*   **Compute on:** Choose between `GPU` (recommended for speed if you have a compatible NVIDIA or AMD card) and `CPU`.
*   **Model:** Select the depth estimation model you want to use. `Depth Anything v2 Base` is a great starting point. Different models have different strengths in quality, speed, and VRAM usage.

### Generation Parameters

*   **BOOST:** A special mode that uses multi-resolution merging to significantly improve the quality and detail of the depth map, especially for the `res101` model. This is very slow and VRAM-intensive.
*   **Match net size to input size:** If checked, the model will process the image at its original resolution. If unchecked, you can specify a custom `Net width` and `Net height` to process at, which can save VRAM but may affect quality.
*   **Tiling mode:** A specialized mode to reduce seams when tiling the depth map. It forces `BOOST` to be off and `Match net size` to be on.

### Output Settings

*   **Save Outputs:** If checked, all generated images will be saved to the `output` folder inside the `stable-diffusion-webui-depthmap-script-main` directory.
*   **Output DepthMap:** The main toggle to generate a depth map image.
*   **Invert:** Flips the depth map colors, making near objects black and far objects white.
*   **Combine...:** Creates a single image with your original input and the generated depth map placed side-by-side (`Horizontal`) or top-and-bottom (`Vertical`).
*   **Clip and renormalize DepthMap:** This allows you to "slice" the depth map. You can clip the near and far planes, effectively focusing on a specific depth range.

### Stereoscopic (3D) Image Generation

*   **Generate stereoscopic (3D) image(s):** Enables the creation of 3D images.
*   **Output:** Choose the format for your 3D image (e.g., `left-right` for VR headsets, `red-cyan-anaglyph` for red/blue 3D glasses).
*   **Divergence:** The main "3D effect" slider. Higher values create a more pronounced 3D effect.
*   **Separation:** Moves the left and right eye images horizontally. Useful for adjusting the "window" through which you are looking.
*   **Gap fill technique:** When creating a 3D effect, gaps appear where objects were occluded. This setting determines the algorithm used to fill those gaps. `polylines_sharp` is the highest quality but slowest.
*   **Balance between eyes:** Determines where distortion from gap-filling is distributed. `0.0` is balanced.

### Normal Map Generation

*   **Generate NormalMap:** Creates a normal map, which is useful for lighting in 3D applications.
*   The various options (`Pre-blur`, `Sobel`, `Post-blur`) allow you to fine-tune the smoothness and sharpness of the resulting normal map.
*   **Invert:** Inverts the direction of the normals.

### 3D Mesh Generation

*   **Generate simple 3D mesh:** Creates a basic `.obj` 3D model from the depth map. It's fast but less detailed.
*   **Generate 3D inpainted mesh:** A much slower but higher-quality process that "inpaints" occluded areas to create a more complete 3D model, saving it as a `.ply` file. This is required for generating videos.

### Video Generation

*   This tab allows you to take a `.ply` mesh created by the "Generate 3D inpainted mesh" option and render a video from it, creating a 3D parallax effect.
*   You can control the camera trajectory, number of frames, FPS, and other settings to create various camera motions like dolly zooms, fly-bys, and circles.

---

## License

This packaging and the custom UI scripts are provided under the **MIT License**.
Use code with caution.

## Credits and Acknowledgements

This project would not be possible without the incredible work of the original authors and the creators of the various models used.

*   **Main Script:** The core functionality comes from the **[stable-diffusion-webui-depthmap-script](https://github.com/thygate/stable-diffusion-webui-depthmap-script)** by **thygate** and its many contributors.
*   **Depth Models:** This tool utilizes code and models from numerous research projects, including:
    *   **MiDaS** and **ZoeDepth** by Intel ISL
    *   **LeReS** by AdelaiDepth
    *   **Marigold** from the Marigold repository
    *   **Depth Anything** and **Depth Anything V2** from the Depth Anything team
*   **3D Inpainting:** Based on "3D Photography using Context-aware Layered Depth Inpainting" by Virginia Tech Vision and Learning Lab.
*   **Background Removal:** Uses `rembg`, which is based on U-2-Net and IS-Net.

Please refer to the `README.md` file inside the `stable-diffusion-webui-depthmap-script-main` folder for a complete and detailed list of acknowledgements and citations for the underlying academic papers.

**Please be aware that the individual AI models downloaded by this application have their own licenses, some of which may be for non-commercial use only.**
