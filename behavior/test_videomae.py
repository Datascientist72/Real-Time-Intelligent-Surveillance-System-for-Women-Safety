from transformers import VideoMAEImageProcessor, VideoMAEForVideoClassification

print("Loading processor...")
processor = VideoMAEImageProcessor.from_pretrained(
    "MCG-NJU/videomae-base"
)

print("Loading model...")
model = VideoMAEForVideoClassification.from_pretrained(
    "MCG-NJU/videomae-base"
)

print("Success!")
print("Labels:", model.config.num_labels)