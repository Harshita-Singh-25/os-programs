def fifo_page_replacement(pages, frame_count):
    frames = []
    page_faults = 0

    print("\nPage\tFrames\t\tStatus")
    print("-------------------------------")
    
    for page in pages:
        if page in frames:
            status = "Hit"
        else:
            status = "Fault"
            page_faults += 1
            if len(frames) < frame_count:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
        
        print(f"{page}\t{frames}\t\t{status}")

    total_pages = len(pages)
    hit_ratio = (total_pages - page_faults) / total_pages

    print("\nSummary:")
    print(f"Total Page Faults: {page_faults}")
    print(f"Total Page Hits: {total_pages - page_faults}")
    print(f"Hit Ratio: {hit_ratio:.2f}")
    print(f"Miss Ratio: {1 - hit_ratio:.2f}")

if __name__ == "__main__":
    pages = [1, 3, 0, 3, 5, 6, 3, 1, 3, 0, 1, 2]
    frame_count = 3

    print("FIFO Page Replacement Algorithm")
    print(f"Page Reference String: {pages}")
    print(f"Number of Frames: {frame_count}")

    fifo_page_replacement(pages, frame_count)
