from statistics import fmean


def main():
    primeira_media = fmean([8, 9, 7])
    segunda_media = fmean([4, 5, 6])

    soma = primeira_media + segunda_media
    media_geral = fmean([primeira_media, segunda_media])

    print(f"Soma das duas medias: {soma}")
    print(f"Media das duas medias: {media_geral}")


if __name__ == "__main__":
    main()
