package javabeans;

import java.io.Serializable;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.Date;
import java.util.Objects;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Temporal;
import javax.persistence.TemporalType;
import javax.persistence.Version;

@Entity
public class Produto implements Serializable {

    private static final long serialVersionUID = 1L;
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;

    @Column(nullable = false, unique = true)
    private int codigo;
    
    @Temporal(TemporalType.DATE)
    @Column(nullable = false)
    private Date data_cadastro;
    
    @Column(nullable = false, precision = 8, scale = 2)
    private BigDecimal valor;

    public Produto() {
        this.id = 0L;
        this.codigo = 0;
        this.data_cadastro = new Date();
        this.valor = new BigDecimal("0.00");
        this.versao = 0;
    }
    
    public Produto(Long id, int codigo, Date data_cadastro, BigDecimal valor, int versao) {
        this.id = id;
        this.codigo = codigo;
        this.data_cadastro = data_cadastro;
        this.valor = valor;
        this.versao = versao;
    }
    
    @Version
    private int versao;
    
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public Date getData_cadastro() {
        return data_cadastro;
    }

    public void setData_cadastro(Date data_cadastro) {
        this.data_cadastro = data_cadastro;
    }

    public BigDecimal getValor() {
        return valor;
    }

    public void setValor(BigDecimal valor) {
        this.valor = valor;
    }

    public int getVersao() {
        return versao;
    }

    public void setVersao(int versao) {
        this.versao = versao;
    }

    @Override
    public int hashCode() {
        int hash = 3;
        hash = 73 * hash + Objects.hashCode(this.id);
        hash = 73 * hash + this.codigo;
        hash = 73 * hash + Objects.hashCode(this.data_cadastro);
        hash = 73 * hash + Objects.hashCode(this.valor);
        hash = 73 * hash + this.versao;
        return hash;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null) {
            return false;
        }
        if (getClass() != obj.getClass()) {
            return false;
        }
        final Produto other = (Produto) obj;
        if (this.codigo != other.codigo) {
            return false;
        }
        if (this.versao != other.versao) {
            return false;
        }
        if (!Objects.equals(this.id, other.id)) {
            return false;
        }
        if (!Objects.equals(this.data_cadastro, other.data_cadastro)) {
            return false;
        }
        if (!Objects.equals(this.valor, other.valor)) {
            return false;
        }
        return true;
    }
    
    @Override
    public String toString() {
        return Integer.toString(this.codigo);
    }
    
}