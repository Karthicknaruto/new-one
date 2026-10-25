import os
import sys
import shutil
import urllib.request

MODEL_URL = "https://raw.githubusercontent.com/Ayush25shrivastava/plant-disease-detection-system/main/trained_model.keras"
DEST_NAME = "trained_plant_disease_model.keras"

def convert_hdf5_to_native_keras(file_path):
    """If file is an HDF5 file with .keras extension, convert it to genuine Keras 3 zip format."""
    try:
        with open(file_path, "rb") as f:
            header = f.read(4)
        if header.startswith(b"\x89HDF"):
            print("Converting legacy HDF5 model to native Keras 3 format...")
            import tensorflow as tf
            temp_h5 = file_path + ".temp.h5"
            shutil.copyfile(file_path, temp_h5)
            model = tf.keras.models.load_model(temp_h5)
            model.save(file_path)
            if os.path.exists(temp_h5):
                os.remove(temp_h5)
            print("[OK] Successfully converted to native Keras 3 format!")
    except Exception as e:
        print(f"[WARNING] Conversion check skipped or failed: {e}")

def download_model(dest_dir=None):
    if dest_dir is None:
        dest_dir = os.path.dirname(os.path.abspath(__file__))
    dest_path = os.path.join(dest_dir, DEST_NAME)

    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 80_000_000:
        # Check if already genuine .keras zip
        with open(dest_path, "rb") as f:
            header = f.read(4)
        if header.startswith(b"\x89HDF"):
            convert_hdf5_to_native_keras(dest_path)
        else:
            print(f"[OK] Model already exists and ready: {dest_path} ({os.path.getsize(dest_path)} bytes)")
        return dest_path

    print(f"Downloading pre-trained model weights (~90 MB) to {DEST_NAME}...")
    
    def reporthook(block_num, block_size, total_size):
        if total_size > 0:
            downloaded = block_num * block_size
            percent = min(100, int(downloaded * 100 / total_size))
            mb_down = downloaded / (1024 * 1024)
            mb_tot = total_size / (1024 * 1024)
            sys.stdout.write(f"\rProgress: [{percent:3d}%] {mb_down:.1f} MB / {mb_tot:.1f} MB")
            sys.stdout.flush()

    try:
        urllib.request.urlretrieve(MODEL_URL, dest_path, reporthook)
        print("\n[SUCCESS] Model downloaded successfully!")
        convert_hdf5_to_native_keras(dest_path)
        return dest_path
    except Exception as e:
        print(f"\n[ERROR] Failed to download model: {e}")
        if os.path.exists(dest_path):
            os.remove(dest_path)
        raise

if __name__ == "__main__":
    download_model()
