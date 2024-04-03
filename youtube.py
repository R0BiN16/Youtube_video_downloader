from pytube import YouTube

# Function to print available streams with their resolutions and audio quality
def print_available_streams(streams):
    print("Available Video and Audio Quality Options:")
    for i, stream in enumerate(streams):
        print(f"{i + 1}. {stream.resolution} ({stream.mime_type}) - Audio: {stream.abr} kbps")

# Function to download the selected stream
def download_selected_stream(stream):
    print("\nDownloading...")
    stream.download()
    print("Download complete!")

# Prompt the user to enter the URL of the video
video_url = input("Enter the URL of the video: ")

# Create a YouTube object with the given video URL
yt = YouTube(video_url)

# Get all streams with both video and audio
available_streams = yt.streams.filter(progressive=True, file_extension='mp4')

# If no progressive streams found, try adaptive streams
if not available_streams:
    available_streams = yt.streams.filter(adaptive=True, file_extension='mp4')

# Print available streams
print_available_streams(available_streams)

# Prompt the user to choose a stream
selected_index = input("Enter the number corresponding to the desired stream to download: ")

# Check if the input is a valid number
if selected_index.isdigit():
    selected_index = int(selected_index) - 1

    # Check if the selected index is valid
    if 0 <= selected_index < len(available_streams):
        selected_stream = available_streams[selected_index]
        download_selected_stream(selected_stream)
    else:
        print("Invalid selection. Please enter a valid number.")
else:
    print("Invalid input. Please enter a number.")
