#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# By Suheel Yousuf Wani


from Bio import SeqIO
import gzip


def statistics(handle):
    print(type(handle))
    try:
        

        
        total_sequences = 0
        total_bases = 0
        base_counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0, 'N': 0}
        quality_scores = []
        seen_sequences = set()
        read_lengths = []

        for record in SeqIO.parse(handle, "fastq"):
            total_sequences += 1
            total_bases += len(record.seq)

            # Calculate base composition
            for base in base_counts:
                base_counts[base] += record.seq.count(base)

            # Calculate quality score statistics
            quality_scores.extend(record.letter_annotations["phred_quality"])

            # Check for duplicate sequences
            seq_str = str(record.seq)
            if seq_str in seen_sequences:
                seen_sequences.add(seq_str)
            else:
                seen_sequences.add(seq_str)

            # Store read lengths
            read_lengths.append(len(record.seq))

        # Calculate GC content
        gc_content = (base_counts['G'] + base_counts['C']) / total_bases

        return {
            "File Size": handle.tell(),
            "Number of Sequences": total_sequences,
            "Sequence Length": {
                "Average": total_bases / total_sequences,
                "Minimum": min(read_lengths),
                "Maximum": max(read_lengths)
            },
            "Base Composition": base_counts,
            "Quality Score Statistics": {
                "Average": sum(quality_scores) / len(quality_scores),
                "Minimum": min(quality_scores),
                "Maximum": max(quality_scores)
            },
            "GC Content": gc_content,
            "Duplicate Sequences": total_sequences - len(seen_sequences),
            "Read Length Distribution": {
                "Minimum": min(read_lengths),
                "Maximum": max(read_lengths)
            },
            "Phred Score Distribution": {
                "Minimum": min(quality_scores),
                "Maximum": max(quality_scores)
            }
        }
    except Exception as e:
        return {"Error": str(e)}
