# 🧪 Case Tester para Introdução à Ciência da Computação II 🎓

Bem-vindo ao **Case Tester**! Este projeto foi criado para facilitar a vida de quem deseja testar automaticamente seus programas na disciplina **Introdução à Ciência da Computação II (SCC0503)**. Vamos automatizar seus testes e deixar a comparação de saídas bem mais prática!

---

## ✨ Motivação

💡 Este script é perfeito para quem quer testar localmente seus códigos sem precisar ficar subindo tudo o tempo todo no **run.codes**. Economize tempo e esforço, rodando seus testes com um simples comando!

---

## 🚀 Funcionalidades

- 📂 **Teste Automático**: Testa múltiplos casos de uma vez.
- 📝 **Comparação de Saídas**: Compara a saída gerada pelo programa com a saída esperada.
- ✅ **Resultados Detalhados**: Exibe quais casos passaram e detalha onde houve falha.
- 🛠️ **Limpeza Automática**: Remove os arquivos temporários após cada execução.

---

## 📦 Como Rodar

1. **Prepare os arquivos**:
   - Crie uma pasta chamada `cases/` no seu diretório.
   - Cada caso de teste deve ter dois arquivos:
     - Um arquivo `.in` para a **entrada**.
     - Um arquivo `.out` para a **saída esperada**.
   - Os arquivos de entrada e saída devem ter o mesmo nome (mudando apenas a extensão).

2. **Execute o tester**:
   - Coloque o script `case_tester.py` no diretório pai da pasta `cases/`.
   - No terminal, execute o seguinte comando:
     ```bash
     python case_tester.py {File2Test}.c
     ```
     Substitua `{File2Test}.c` pelo nome do arquivo que você deseja testar.

3. **Veja os resultados**:
   - Para cada teste, o script dirá se passou (`✅`) ou falhou (`❌`).
   - Em caso de falha, ele mostrará:
     - 📥 A entrada do teste.
     - 📤 A saída esperada.
     - ⚠️ A saída obtida pelo seu programa.

    **Exemplo:**
    ```bash
            Caso 01: ✅
            Caso 02: ❌
            ======== Detalhes ========
            Entrada: 6 4
            Saída esperada: 10
            Saída obtida: 8
            ==========================
    ```


---

## ⚠️ Observações, Resultado Esperado e Autor

- A pasta `cases/` deve estar no mesmo nível do script `case_tester.py`.
- O script compila automaticamente o arquivo `.c` fornecido.
- Verifique se os nomes dos arquivos de teste estão corretos (devem ser iguais, exceto pelas extensões `.in` e `.out`).
- O resultado será uma lista de testes que passaram (`✅`) ou falharam (`❌`), com detalhes sobre a entrada, saída esperada e saída obtida, em caso de falha.

Desenvolvido por **Miguel Filippo Rocha Calhabeu** para a disciplina **Introdução à Ciência da Computação II** (SCC0503) na **USP**.

Se você achou este projeto útil, sinta-se à vontade para dar ⭐ no repositório! 😄
