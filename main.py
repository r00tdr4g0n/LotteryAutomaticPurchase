import lottery
import annuity


if __name__ == '__main__':
    dh = lottery.Lottery()
    ann = annuity.Annuity(dh.GetDriver())

    dh.Login()
    ann.OpenAnnuity()
    ann.BuyAnnuity()
