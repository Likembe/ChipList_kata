class ChipList:
    def __init__(self, chips=None, max_chips_displayed=None, max_text_length=None):
        self.chips = chips if chips is not None else []
        self.max_chips_displayed = max_chips_displayed
        self.max_text_length = max_text_length

    def display_chips(self):
        if not self.chips or not self.max_chips_displayed or not self.max_text_length:
            return []

        rendered_chips = []
        exceeding_chips = []

        for i, chip in enumerate(self.chips):
            label = chip["label"]

            # Trim text to max_text_length characters and add ellipsis if needed
            trimmed_label = label[:self.max_text_length] + "…" if len(label) > self.max_text_length else label

            # Render chips up to the max_chips_displayed limit
            if i < self.max_chips_displayed:
                rendered_chips.append(trimmed_label)
            else:
                exceeding_chips.append(label)

        if len(exceeding_chips) > 0:
            exceeding_text = f"+{len(exceeding_chips)} more items"
            return rendered_chips + [exceeding_text]
        else:
            return rendered_chips

# Sample list of chips
sample_chips = [
    { "label": "123456" },
    { "label": "1234567" },
    { "label": "12345678" },
    { "label": "12345" },
    { "label": "123456789" }
]

# Create a ChipList instance and specify the max_chips_displayed and max_text_length
chip_list = ChipList(chips=sample_chips, max_chips_displayed=3, max_text_length=6)

# Display the chips
displayed_chips = chip_list.display_chips()
for i, chip in enumerate(displayed_chips):
    print(f"{i + 1}. {chip}")
