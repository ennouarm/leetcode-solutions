from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 1
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r+=1
        return maxP

if "__name__" == "__main__":
    solution = Solution()
    resultat = solution.maxProfit([6,1,5,7,4,3])
    
    # 💡 MODIFICATION CLÉ : Écriture dans un fichier
    try:
        with open("result_max_profit.txt", "w") as f:
            f.write(f"Le profit maximum calculé est : {resultat}\n")
            f.write("Ce fichier confirme que le code a été exécuté avec succès.")
        
        # Laissez le print() au cas où il fonctionne subitement
        print(f"Résultat trouvé (dans le fichier) : {resultat}")
        
    except Exception as e:
        # En cas d'erreur de permission d'écriture
        print(f"Erreur lors de l'écriture du fichier : {e}")