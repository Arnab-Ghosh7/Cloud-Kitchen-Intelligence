import os
import shutil
import zipfile

def pack():
    submission_dir = r"e:\Experifo Labs\submission"
    root_dir = r"e:\Experifo Labs"
    
    print("Preparing final submission package...")

    files_to_copy = [
        (os.path.join(root_dir, "data_pipeline.ipynb"), os.path.join(submission_dir, "data_pipeline.ipynb")),
        (os.path.join(root_dir, "src", "data_pipeline.py"), os.path.join(submission_dir, "data_pipeline.py")),
        (os.path.join(root_dir, "src", "generate_screenshots.py"), os.path.join(submission_dir, "generate_screenshots.py")),
        (os.path.join(root_dir, "src", "generate_report.py"), os.path.join(submission_dir, "generate_report.py")),
        (os.path.join(root_dir, "src", "query_exercises.sql"), os.path.join(submission_dir, "exercise_queries.sql")),
        (os.path.join(root_dir, "requirements.txt"), os.path.join(submission_dir, "requirements.txt")),
    ]

    for src, dst in files_to_copy:
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"Copied: {os.path.basename(src)} -> {dst}")
        else:
            print(f"Warning: Source not found: {src}")

    src_dashboard = os.path.join(root_dir, "src", "dashboard")
    dst_dashboard = os.path.join(submission_dir, "dashboard")
    
    if os.path.exists(dst_dashboard):
        shutil.rmtree(dst_dashboard)
        
    shutil.copytree(src_dashboard, dst_dashboard)
    print("Copied interactive dashboard folder to submission/dashboard!")

    zip_path = os.path.join(root_dir, "submission.zip")
    if os.path.exists(zip_path):
        os.remove(zip_path)
        print("Removed existing submission.zip")

    print("Creating ZIP file...")
    shutil.make_archive(os.path.join(root_dir, "submission"), 'zip', submission_dir)
    print(f"Submission ZIP compiled successfully! Saved to: {zip_path}")

if __name__ == "__main__":
    pack()
