# ================================================================= #
# THE DEFINITIVE FIX: MONKEY-PATCHING
# ================================================================= #
import sys
import os
import time

# 1. Fix the Python Path for the embeddable distribution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

# 2. Monkey-patch the 'huggingface_hub' library.
try:
    import huggingface_hub
    if not hasattr(huggingface_hub, 'cached_download'):
        huggingface_hub.cached_download = huggingface_hub.hf_hub_download
    print("Monkey-patch for 'huggingface_hub.cached_download' applied successfully.")
except Exception as e:
    print(f"Could not apply monkey-patch. This might cause issues. Error: {e}")
# ================================================================= #

# Now, we can safely import and run the application.
try:
    import src.common_ui
    print("Successfully imported 'src.common_ui'")
except ImportError as e:
    print("FATAL: Could not import 'src.common_ui' even after patching.")
    print(f"Original error: {e}")
    input("Press Enter to exit...")
    sys.exit(1)

def launch_app(share=False, listen=False):
    server_name = "0.0.0.0" if listen else None
    print("Launching Gradio UI...")
    # We will let this run in the background thread. The script will be kept alive by the code below.
    src.common_ui.on_ui_tabs().launch(share=share, server_name=server_name)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--share", help="Create public link", action='store_true')
    parser.add_argument("--listen", help="Listen on 0.0.0.0", action='store_true')
    args = parser.parse_args()
    
    # Start the Gradio app. It will run in the background.
    launch_app(share=args.share, listen=args.listen)

    # ================================================================= #
    # THE FIX TO KEEP THE SCRIPT ALIVE
    # This loop will run forever, keeping the script (and the command prompt)
    # open until you manually close it (e.g., with Ctrl+C or by closing the window).
    # ================================================================= #
    print("\nGradio UI is running. Press Ctrl+C in this window to stop the server.")
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Stopping server...")