export interface ConsumerQuestion {
  id: string;
  title: string;
  prompt: string;
  how_to_answer: string;

  media?: {
    type: "image" | "video";
    url: string;
    alt?: string;
  };

  // Always present (age uses an empty array)
  options: { value: string; label: string }[];

  // Optional special type (e.g. number input)
  type?: "number";

  // Mapping to clinical engine
  maps_to: {
    section: "patient" | "pain" | "red_flags";
    field: string;
  };
}
